"""adding_version

Revision ID: 5cf63f567a62
Revises: 2e58cc00009b
Create Date: 2020-08-26 17:16:57.006971

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5cf63f567a62'
down_revision = '2e58cc00009b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_login_options_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('login_source', sa.String(length=20), autoincrement=False, nullable=True),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('is_active', sa.Boolean(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_account_login_options_version_end_transaction_id'), 'account_login_options_version',
                    ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_account_login_options_version_operation_type'), 'account_login_options_version',
                    ['operation_type'], unique=False)
    op.create_index(op.f('ix_account_login_options_version_transaction_id'), 'account_login_options_version',
                    ['transaction_id'], unique=False)
    op.create_table('account_payment_settings_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('preferred_payment_code', sa.String(length=15), autoincrement=False, nullable=True),
                    sa.Column('bcol_user_id', sa.String(length=20), autoincrement=False, nullable=True),
                    sa.Column('bcol_account_id', sa.String(length=20), autoincrement=False, nullable=True),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('is_active', sa.Boolean(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_account_payment_settings_version_end_transaction_id'), 'account_payment_settings_version',
                    ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_account_payment_settings_version_operation_type'), 'account_payment_settings_version',
                    ['operation_type'], unique=False)
    op.create_index(op.f('ix_account_payment_settings_version_transaction_id'), 'account_payment_settings_version',
                    ['transaction_id'], unique=False)
    op.create_table('activity',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('verb', sa.Unicode(length=255), nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), nullable=False),
                    sa.Column('data', sqlalchemy_utils.types.json.JSONType(), nullable=True),
                    sa.Column('object_type', sa.String(length=255), nullable=True),
                    sa.Column('object_id', sa.BigInteger(), nullable=True),
                    sa.Column('object_tx_id', sa.BigInteger(), nullable=True),
                    sa.Column('target_type', sa.String(length=255), nullable=True),
                    sa.Column('target_id', sa.BigInteger(), nullable=True),
                    sa.Column('target_tx_id', sa.BigInteger(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_activity_transaction_id'), 'activity', ['transaction_id'], unique=False)
    op.create_table('affidavit_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('document_id', sa.String(length=60), autoincrement=False, nullable=True),
                    sa.Column('issuer', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('status_code', sa.String(length=15), autoincrement=False, nullable=True),
                    sa.Column('decision_made_by', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('decision_made_on', sa.DateTime(), autoincrement=False, nullable=True),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_affidavit_version_document_id'), 'affidavit_version', ['document_id'], unique=False)
    op.create_index(op.f('ix_affidavit_version_end_transaction_id'), 'affidavit_version', ['end_transaction_id'],
                    unique=False)
    op.create_index(op.f('ix_affidavit_version_operation_type'), 'affidavit_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_affidavit_version_transaction_id'), 'affidavit_version', ['transaction_id'], unique=False)
    op.create_table('affiliation_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('entity_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_affiliation_version_end_transaction_id'), 'affiliation_version', ['end_transaction_id'],
                    unique=False)
    op.create_index(op.f('ix_affiliation_version_operation_type'), 'affiliation_version', ['operation_type'],
                    unique=False)
    op.create_index(op.f('ix_affiliation_version_transaction_id'), 'affiliation_version', ['transaction_id'],
                    unique=False)
    op.create_table('contact_link_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('contact_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('entity_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('affidavit_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_contact_link_version_end_transaction_id'), 'contact_link_version', ['end_transaction_id'],
                    unique=False)
    op.create_index(op.f('ix_contact_link_version_operation_type'), 'contact_link_version', ['operation_type'],
                    unique=False)
    op.create_index(op.f('ix_contact_link_version_transaction_id'), 'contact_link_version', ['transaction_id'],
                    unique=False)
    op.create_table('contact_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('street', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('street_additional', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('city', sa.String(length=100), autoincrement=False, nullable=True),
                    sa.Column('region', sa.String(length=100), autoincrement=False, nullable=True),
                    sa.Column('country', sa.String(length=20), autoincrement=False, nullable=True),
                    sa.Column('postal_code', sa.String(length=10), autoincrement=False, nullable=True),
                    sa.Column('delivery_instructions', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('phone', sa.String(length=15), autoincrement=False, nullable=True),
                    sa.Column('phone_extension', sa.String(length=10), autoincrement=False, nullable=True),
                    sa.Column('email', sa.String(length=100), autoincrement=False, nullable=True),
                    sa.Column('entity_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_contact_version_end_transaction_id'), 'contact_version', ['end_transaction_id'],
                    unique=False)
    op.create_index(op.f('ix_contact_version_operation_type'), 'contact_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_contact_version_street'), 'contact_version', ['street'], unique=False)
    op.create_index(op.f('ix_contact_version_transaction_id'), 'contact_version', ['transaction_id'], unique=False)
    op.create_table('membership_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('membership_type_code', sa.String(length=15), autoincrement=False, nullable=True),
                    sa.Column('status', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_membership_version_end_transaction_id'), 'membership_version', ['end_transaction_id'],
                    unique=False)
    op.create_index(op.f('ix_membership_version_operation_type'), 'membership_version', ['operation_type'],
                    unique=False)
    op.create_index(op.f('ix_membership_version_transaction_id'), 'membership_version', ['transaction_id'],
                    unique=False)
    op.create_table('org_settings_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('setting', sa.String(length=100), autoincrement=False, nullable=True),
                    sa.Column('enabled', sa.Boolean(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_org_settings_version_end_transaction_id'), 'org_settings_version', ['end_transaction_id'],
                    unique=False)
    op.create_index(op.f('ix_org_settings_version_operation_type'), 'org_settings_version', ['operation_type'],
                    unique=False)
    op.create_index(op.f('ix_org_settings_version_transaction_id'), 'org_settings_version', ['transaction_id'],
                    unique=False)
    op.create_table('org_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('type_code', sa.String(length=15), autoincrement=False, nullable=True),
                    sa.Column('status_code', sa.String(length=30), autoincrement=False, nullable=True),
                    sa.Column('name', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('access_type', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('billable', sa.Boolean(), autoincrement=False, nullable=True),
                    sa.Column('decision_made_by', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('decision_made_on', sa.DateTime(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_org_version_access_type'), 'org_version', ['access_type'], unique=False)
    op.create_index(op.f('ix_org_version_end_transaction_id'), 'org_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_org_version_name'), 'org_version', ['name'], unique=False)
    op.create_index(op.f('ix_org_version_operation_type'), 'org_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_org_version_transaction_id'), 'org_version', ['transaction_id'], unique=False)
    op.create_table('product_subscription_role_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('product_subscription_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('product_role_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_product_subscription_role_version_end_transaction_id'),
                    'product_subscription_role_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_product_subscription_role_version_operation_type'), 'product_subscription_role_version',
                    ['operation_type'], unique=False)
    op.create_index(op.f('ix_product_subscription_role_version_transaction_id'), 'product_subscription_role_version',
                    ['transaction_id'], unique=False)
    op.create_table('product_subscription_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('org_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('product_code', sa.String(length=15), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_product_subscription_version_end_transaction_id'), 'product_subscription_version',
                    ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_product_subscription_version_operation_type'), 'product_subscription_version',
                    ['operation_type'], unique=False)
    op.create_index(op.f('ix_product_subscription_version_transaction_id'), 'product_subscription_version',
                    ['transaction_id'], unique=False)
    op.create_table('transaction',
                    sa.Column('issued_at', sa.DateTime(), nullable=True),
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('remote_addr', sa.String(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('username', sa.String(length=100), autoincrement=False, nullable=True),
                    sa.Column('first_name', sa.String(length=200), autoincrement=False, nullable=True),
                    sa.Column('last_name', sa.String(length=200), autoincrement=False, nullable=True),
                    sa.Column('email', sa.String(length=200), autoincrement=False, nullable=True),
                    sa.Column('keycloak_guid', postgresql.UUID(as_uuid=True), autoincrement=False, nullable=True),
                    sa.Column('roles', sa.String(length=1000), autoincrement=False, nullable=True),
                    sa.Column('is_terms_of_use_accepted', sa.Boolean(), autoincrement=False, nullable=True),
                    sa.Column('terms_of_use_accepted_version', sa.String(length=10), autoincrement=False,
                              nullable=True),
                    sa.Column('type', sa.String(length=200), autoincrement=False, nullable=True),
                    sa.Column('status', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('idp_userid', sa.String(length=256), autoincrement=False, nullable=True),
                    sa.Column('login_source', sa.String(length=200), autoincrement=False, nullable=True),
                    sa.Column('login_time', sa.DateTime(), autoincrement=False, nullable=True),
                    sa.Column('created_by_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_user_version_email'), 'user_version', ['email'], unique=False)
    op.create_index(op.f('ix_user_version_end_transaction_id'), 'user_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_user_version_first_name'), 'user_version', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_version_idp_userid'), 'user_version', ['idp_userid'], unique=False)
    op.create_index(op.f('ix_user_version_last_name'), 'user_version', ['last_name'], unique=False)
    op.create_index(op.f('ix_user_version_operation_type'), 'user_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_user_version_transaction_id'), 'user_version', ['transaction_id'], unique=False)
    op.create_index(op.f('ix_user_version_username'), 'user_version', ['username'], unique=False)

    op.execute('update documents set content_type=\'text/html\' where type=\'termsofuse\'')

    op.alter_column('documents', 'content_type',
                    existing_type=sa.VARCHAR(length=50),
                    type_=sa.String(length=20),
                    nullable=False)
    op.alter_column('membership_type', 'display_name',
                    existing_type=sa.VARCHAR(length=50),
                    type_=sa.String(length=100),
                    existing_nullable=True)
    op.add_column('user', sa.Column('login_time', sa.DateTime(), nullable=True))
    op.alter_column('user', 'login_source',
                    existing_type=sa.VARCHAR(length=20),
                    type_=sa.String(length=200),
                    existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'login_source',
                    existing_type=sa.String(length=200),
                    type_=sa.VARCHAR(length=20),
                    existing_nullable=True)
    op.drop_column('user', 'login_time')
    op.alter_column('membership_type', 'display_name',
                    existing_type=sa.String(length=100),
                    type_=sa.VARCHAR(length=50),
                    existing_nullable=True)
    op.alter_column('documents', 'content_type',
                    existing_type=sa.String(length=20),
                    type_=sa.VARCHAR(length=50),
                    nullable=True)
    op.drop_index(op.f('ix_user_version_username'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_transaction_id'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_operation_type'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_last_name'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_idp_userid'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_first_name'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_end_transaction_id'), table_name='user_version')
    op.drop_index(op.f('ix_user_version_email'), table_name='user_version')
    op.drop_table('user_version')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_product_subscription_version_transaction_id'), table_name='product_subscription_version')
    op.drop_index(op.f('ix_product_subscription_version_operation_type'), table_name='product_subscription_version')
    op.drop_index(op.f('ix_product_subscription_version_end_transaction_id'), table_name='product_subscription_version')
    op.drop_table('product_subscription_version')
    op.drop_index(op.f('ix_product_subscription_role_version_transaction_id'),
                  table_name='product_subscription_role_version')
    op.drop_index(op.f('ix_product_subscription_role_version_operation_type'),
                  table_name='product_subscription_role_version')
    op.drop_index(op.f('ix_product_subscription_role_version_end_transaction_id'),
                  table_name='product_subscription_role_version')
    op.drop_table('product_subscription_role_version')
    op.drop_index(op.f('ix_org_version_transaction_id'), table_name='org_version')
    op.drop_index(op.f('ix_org_version_operation_type'), table_name='org_version')
    op.drop_index(op.f('ix_org_version_name'), table_name='org_version')
    op.drop_index(op.f('ix_org_version_end_transaction_id'), table_name='org_version')
    op.drop_index(op.f('ix_org_version_access_type'), table_name='org_version')
    op.drop_table('org_version')
    op.drop_index(op.f('ix_org_settings_version_transaction_id'), table_name='org_settings_version')
    op.drop_index(op.f('ix_org_settings_version_operation_type'), table_name='org_settings_version')
    op.drop_index(op.f('ix_org_settings_version_end_transaction_id'), table_name='org_settings_version')
    op.drop_table('org_settings_version')
    op.drop_index(op.f('ix_membership_version_transaction_id'), table_name='membership_version')
    op.drop_index(op.f('ix_membership_version_operation_type'), table_name='membership_version')
    op.drop_index(op.f('ix_membership_version_end_transaction_id'), table_name='membership_version')
    op.drop_table('membership_version')
    op.drop_index(op.f('ix_contact_version_transaction_id'), table_name='contact_version')
    op.drop_index(op.f('ix_contact_version_street'), table_name='contact_version')
    op.drop_index(op.f('ix_contact_version_operation_type'), table_name='contact_version')
    op.drop_index(op.f('ix_contact_version_end_transaction_id'), table_name='contact_version')
    op.drop_table('contact_version')
    op.drop_index(op.f('ix_contact_link_version_transaction_id'), table_name='contact_link_version')
    op.drop_index(op.f('ix_contact_link_version_operation_type'), table_name='contact_link_version')
    op.drop_index(op.f('ix_contact_link_version_end_transaction_id'), table_name='contact_link_version')
    op.drop_table('contact_link_version')
    op.drop_index(op.f('ix_affiliation_version_transaction_id'), table_name='affiliation_version')
    op.drop_index(op.f('ix_affiliation_version_operation_type'), table_name='affiliation_version')
    op.drop_index(op.f('ix_affiliation_version_end_transaction_id'), table_name='affiliation_version')
    op.drop_table('affiliation_version')
    op.drop_index(op.f('ix_affidavit_version_transaction_id'), table_name='affidavit_version')
    op.drop_index(op.f('ix_affidavit_version_operation_type'), table_name='affidavit_version')
    op.drop_index(op.f('ix_affidavit_version_end_transaction_id'), table_name='affidavit_version')
    op.drop_index(op.f('ix_affidavit_version_document_id'), table_name='affidavit_version')
    op.drop_table('affidavit_version')
    op.drop_index(op.f('ix_activity_transaction_id'), table_name='activity')
    op.drop_table('activity')
    op.drop_index(op.f('ix_account_payment_settings_version_transaction_id'),
                  table_name='account_payment_settings_version')
    op.drop_index(op.f('ix_account_payment_settings_version_operation_type'),
                  table_name='account_payment_settings_version')
    op.drop_index(op.f('ix_account_payment_settings_version_end_transaction_id'),
                  table_name='account_payment_settings_version')
    op.drop_table('account_payment_settings_version')
    op.drop_index(op.f('ix_account_login_options_version_transaction_id'), table_name='account_login_options_version')
    op.drop_index(op.f('ix_account_login_options_version_operation_type'), table_name='account_login_options_version')
    op.drop_index(op.f('ix_account_login_options_version_end_transaction_id'),
                  table_name='account_login_options_version')
    op.drop_table('account_login_options_version')
    # ### end Alembic commands ###
