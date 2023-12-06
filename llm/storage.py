from phi.storage.conversation.postgres import PgConversationStorage

from db.session import db_url

mock_conversation_storage = PgConversationStorage(
    table_name="mock_conversations",
    db_url=db_url,
)

test_conversation_storage = PgConversationStorage(
    table_name="test_conversations",
    db_url=db_url,
)
