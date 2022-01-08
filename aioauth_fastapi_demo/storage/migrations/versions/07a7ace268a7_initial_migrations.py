"""Initial migrations

Revision ID: 07a7ace268a7
Revises:
Create Date: 2021-10-02 22:50:10.418498

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "07a7ace268a7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.Column("is_blocked", sa.Boolean(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("username", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("password", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=True)
    op.create_index(op.f("ix_users_is_active"), "users", ["is_active"], unique=False)
    op.create_index(op.f("ix_users_is_blocked"), "users", ["is_blocked"], unique=False)
    op.create_index(
        op.f("ix_users_is_superuser"), "users", ["is_superuser"], unique=False
    )
    op.create_index(op.f("ix_users_password"), "users", ["password"], unique=False)
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=True)
    op.create_table(
        "authorizationcode",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("code", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("client_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("redirect_uri", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("response_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("scope", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("auth_time", sa.Integer(), nullable=False),
        sa.Column("expires_in", sa.Integer(), nullable=False),
        sa.Column("code_challenge", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "code_challenge_method", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("nonce", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_authorizationcode_auth_time"),
        "authorizationcode",
        ["auth_time"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_client_id"),
        "authorizationcode",
        ["client_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_code"), "authorizationcode", ["code"], unique=False
    )
    op.create_index(
        op.f("ix_authorizationcode_code_challenge"),
        "authorizationcode",
        ["code_challenge"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_code_challenge_method"),
        "authorizationcode",
        ["code_challenge_method"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_expires_in"),
        "authorizationcode",
        ["expires_in"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_id"), "authorizationcode", ["id"], unique=True
    )
    op.create_index(
        op.f("ix_authorizationcode_nonce"), "authorizationcode", ["nonce"], unique=False
    )
    op.create_index(
        op.f("ix_authorizationcode_redirect_uri"),
        "authorizationcode",
        ["redirect_uri"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_response_type"),
        "authorizationcode",
        ["response_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_authorizationcode_scope"), "authorizationcode", ["scope"], unique=False
    )
    op.create_index(
        op.f("ix_authorizationcode_user_id"),
        "authorizationcode",
        ["user_id"],
        unique=False,
    )
    op.create_table(
        "client",
        sa.Column("grant_types", sa.ARRAY(sa.String()), nullable=True),
        sa.Column("response_types", sa.ARRAY(sa.String()), nullable=True),
        sa.Column("redirect_uris", sa.ARRAY(sa.String()), nullable=True),
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("client_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("client_secret", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("scope", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_client_client_id"), "client", ["client_id"], unique=False)
    op.create_index(
        op.f("ix_client_client_secret"), "client", ["client_secret"], unique=False
    )
    op.create_index(op.f("ix_client_id"), "client", ["id"], unique=True)
    op.create_index(op.f("ix_client_scope"), "client", ["scope"], unique=False)
    op.create_index(op.f("ix_client_user_id"), "client", ["user_id"], unique=False)
    op.create_table(
        "token",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("access_token", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("refresh_token", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("scope", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("issued_at", sa.Integer(), nullable=False),
        sa.Column("expires_in", sa.Integer(), nullable=False),
        sa.Column("refresh_token_expires_in", sa.Integer(), nullable=False),
        sa.Column("client_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("token_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("revoked", sa.Boolean(), nullable=False),
        sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_token_access_token"), "token", ["access_token"], unique=False
    )
    op.create_index(op.f("ix_token_client_id"), "token", ["client_id"], unique=False)
    op.create_index(op.f("ix_token_expires_in"), "token", ["expires_in"], unique=False)
    op.create_index(op.f("ix_token_id"), "token", ["id"], unique=True)
    op.create_index(op.f("ix_token_issued_at"), "token", ["issued_at"], unique=False)
    op.create_index(
        op.f("ix_token_refresh_token"), "token", ["refresh_token"], unique=False
    )
    op.create_index(
        op.f("ix_token_refresh_token_expires_in"),
        "token",
        ["refresh_token_expires_in"],
        unique=False,
    )
    op.create_index(op.f("ix_token_revoked"), "token", ["revoked"], unique=False)
    op.create_index(op.f("ix_token_scope"), "token", ["scope"], unique=False)
    op.create_index(op.f("ix_token_token_type"), "token", ["token_type"], unique=False)
    op.create_index(op.f("ix_token_user_id"), "token", ["user_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_token_user_id"), table_name="token")
    op.drop_index(op.f("ix_token_token_type"), table_name="token")
    op.drop_index(op.f("ix_token_scope"), table_name="token")
    op.drop_index(op.f("ix_token_revoked"), table_name="token")
    op.drop_index(op.f("ix_token_refresh_token_expires_in"), table_name="token")
    op.drop_index(op.f("ix_token_refresh_token"), table_name="token")
    op.drop_index(op.f("ix_token_issued_at"), table_name="token")
    op.drop_index(op.f("ix_token_id"), table_name="token")
    op.drop_index(op.f("ix_token_expires_in"), table_name="token")
    op.drop_index(op.f("ix_token_client_id"), table_name="token")
    op.drop_index(op.f("ix_token_access_token"), table_name="token")
    op.drop_table("token")
    op.drop_index(op.f("ix_client_user_id"), table_name="client")
    op.drop_index(op.f("ix_client_scope"), table_name="client")
    op.drop_index(op.f("ix_client_id"), table_name="client")
    op.drop_index(op.f("ix_client_client_secret"), table_name="client")
    op.drop_index(op.f("ix_client_client_id"), table_name="client")
    op.drop_table("client")
    op.drop_index(op.f("ix_authorizationcode_user_id"), table_name="authorizationcode")
    op.drop_index(op.f("ix_authorizationcode_scope"), table_name="authorizationcode")
    op.drop_index(
        op.f("ix_authorizationcode_response_type"), table_name="authorizationcode"
    )
    op.drop_index(
        op.f("ix_authorizationcode_redirect_uri"), table_name="authorizationcode"
    )
    op.drop_index(op.f("ix_authorizationcode_nonce"), table_name="authorizationcode")
    op.drop_index(op.f("ix_authorizationcode_id"), table_name="authorizationcode")
    op.drop_index(
        op.f("ix_authorizationcode_expires_in"), table_name="authorizationcode"
    )
    op.drop_index(
        op.f("ix_authorizationcode_code_challenge_method"),
        table_name="authorizationcode",
    )
    op.drop_index(
        op.f("ix_authorizationcode_code_challenge"), table_name="authorizationcode"
    )
    op.drop_index(op.f("ix_authorizationcode_code"), table_name="authorizationcode")
    op.drop_index(
        op.f("ix_authorizationcode_client_id"), table_name="authorizationcode"
    )
    op.drop_index(
        op.f("ix_authorizationcode_auth_time"), table_name="authorizationcode"
    )
    op.drop_table("authorizationcode")
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_index(op.f("ix_users_password"), table_name="users")
    op.drop_index(op.f("ix_users_is_superuser"), table_name="users")
    op.drop_index(op.f("ix_users_is_blocked"), table_name="users")
    op.drop_index(op.f("ix_users_is_active"), table_name="users")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###
