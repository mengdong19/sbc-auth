<template>
  <div>
    <template>
      <v-card
        outlined
        hover
        class="product-card py-8 px-5 mb-4 elevation-1"
        :class="[{'px-8': icon === ''}, {'processing-card' : !isRequesting}]"
        :data-test="`div-product-${productDetails.title}`"
      >
        <div>
          <header class="d-flex align-center">
            <div class="product-icon-container mt-n2 mr-2" v-if="!isRequesting">
              <v-icon meduim color="primary">{{icon}}</v-icon>
            </div>
            <div class="pr-8 ">
              <h3 class="title font-weight-bold product-title mt-n1">{{productDetails.name}}</h3>
              <div>{{productSubTitle}}</div>
            </div>
            <v-icon large v-if="isRequestNow"
            class="ml-auto"
            @click="requestNow()">mdi-close</v-icon>
            <v-btn
            v-else
              large
              depressed
              color="primary"
              width="120"
              class="font-weight-bold ml-auto"
              :outlined="!isApproved"
              :aria-label="`Select  ${productDetails.name}`"
              :data-test="`btn-productDetails-${productDetails.name}`"
              @click="requestNow()"
            >
              <span>{{label}}</span>
            </v-btn>
          </header>

          <div class="product-card-contents">
            <v-expand-transition>
              <div v-if="isRequestNow" class="pt-7">
                <ProductTos
                  :userName="userName"
                  :orgName="orgName"
                  @tos-status-changed="tosChanged"
                />
                <v-divider class="my-7"></v-divider>
                <div class="form__btns d-flex">
                  <v-btn
                    large
                    class="request-btn"
                    color="primary"
                    :disabled="isDisableSaveBtn"
                    @click="requestProduct"
                    :loading="isLoading"
                  >
                    <span class="save-btn__label">Request</span>
                  </v-btn>

                    <v-btn
                    large
                    class="request-cancel-btn ml-3"
                    color="gray"
                    @click="cancel"
                    :loading="isLoading"
                  >
                    <span class="save-btn__label">Cancel</span>
                  </v-btn>
                </div>
              </div>
            </v-expand-transition>
          </div>
        </div>
      </v-card>
    </template>
  </div>
</template>

<script lang="ts">
import { Component, Emit, Prop, Vue, Watch } from 'vue-property-decorator'
import { OrgProduct } from '@/models/Organization'
import ProductTos from '@/components/auth/common/ProductTOS.vue'
import { productStatus } from '@/util/constants'

@Component({
  components: {
    ProductTos
  }
})
export default class Product extends Vue {
  @Prop({ default: undefined }) productDetails: OrgProduct
  @Prop({ default: '' }) userName: string
  @Prop({ default: '' }) orgName: string
  private isRequestNow: boolean = false
  private termsAccepted: boolean = false
  public isLoading : boolean = false
  public label = 'Reqeust'
  public productSubTitle = ''
  public icon = ''
  public isApproved = false
  public isPending = false
  public isRejected = false
  public isRequesting = false

  @Watch('productDetails')
  onProductChange (newProd:OrgProduct, oldProduct:OrgProduct) {
    if (newProd.subscriptionStatus !== oldProduct.subscriptionStatus) {
      this.isRequestNow = false
    }
    this.setupProductDetails(newProd)
  }
  get isDisableSaveBtn () {
    return !this.isFormvalid()
  }

  setupProductDetails (productDetails) {
    const { subscriptionStatus, name, description } = productDetails
    // resetiing all values first
    this.isApproved = false
    this.isPending = false
    this.isRejected = false
    this.isRequesting = false

    if (subscriptionStatus === productStatus.PENDING_STAFF_REVIEW) {
      this.label = 'Pending'
      this.icon = 'mdi-clock-outline'
      this.isPending = true
      this.productSubTitle = 'Your request is under review (pending)'
    } else if (subscriptionStatus === productStatus.REJECTED) {
      this.label = 'Rejected'
      this.icon = 'mdi-clock-outline'
      this.productSubTitle = 'Your request is rejected (rejected)'
      this.isRejected = true
    } else if (subscriptionStatus === productStatus.ACTIVE) {
      this.label = 'Approved'
      this.icon = 'mdi-check-circle'
      this.isApproved = true
      this.productSubTitle = `This account have access to ${name}`
    } else {
      this.isRequesting = true
      this.productSubTitle = description
    }
  }

  public mounted () {
    this.setupProductDetails(this.productDetails)
  }

  public requestNow () {
    const { subscriptionStatus } = this.productDetails
    // need to expand only if not already requested
    if (subscriptionStatus === '' || subscriptionStatus === productStatus.NOT_SUBSCRIBED) {
      this.isRequestNow = !this.isRequestNow
    }
  }

  public tosChanged (termsAccepted:boolean) {
    this.termsAccepted = termsAccepted
  }

  @Emit('set-selected-product')
  public requestProduct () {
    // this.tosChanged()
    if (this.isFormvalid()) {
      return this.productDetails
    }
    return false
  }
  public isFormvalid () {
    return this.termsAccepted
  }
  cancel () {
    this.requestNow()
  }
}
</script>

<style lang="scss" scoped>
.form__btns {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  margin-top: 2rem;

  .v-btn {
    width: 6rem;
  }
}

.product-card {
  transition: all ease-out 0.2s;

  &:hover {
    border-color: var(--v-primary-base) !important;
  }

  &.selected {
    box-shadow: 0 0 0 2px inset var(--v-primary-base), 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12) !important;
  }
  &.processing-card{
    border-color: var(--v-primary-base) !important;
  }

}

.theme--light.v-card.v-card--outlined.selected {
  border-color: var(--v-primary-base);
}

.product-icon-container {
  flex: 0 0 auto;
}
.label-color {
  color:  rgba(0,0,0,.87) !important;
}
.pad-form-container {
  max-width: 75ch;
}
.terms-error{
  color: var(--v-error-base) !important;
  font-size: 16px;
  font-weight: bold;
  display: flex;
}
.error-color{
  color: var(--v-error-base) !important;
}
</style>
