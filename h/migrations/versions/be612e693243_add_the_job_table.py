"""Add the job table."""
from alembic import op
from sqlalchemy import Column, DateTime, UnicodeText, func, text
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "be612e693243"
down_revision = "64039842150a"


def upgrade():
    op.create_table(
        "job",
        Column(
            "id",
            UUID(),
            server_default=func.uuid_generate_v1mc(),
            primary_key=True,
        ),
        Column("enqueued_at", DateTime, nullable=False, server_default=func.now()),
        Column("scheduled_at", DateTime, nullable=False, server_default=func.now()),
        Column("tag", UnicodeText, nullable=False),
        Column(
            "kwargs",
            JSONB,
            server_default=text("'{}'::jsonb"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("job")
