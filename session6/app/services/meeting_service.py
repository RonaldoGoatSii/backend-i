import logging
from uuid import uuid4
from app.domain.models import Meeting
from app.services.memory_store import meetings

logger = logging.getLogger(__name__)


def create_meeting(title: str, date: str, owner: str) -> Meeting:
    logger.info("Creating meeting")

    meeting = Meeting(
        id=str(uuid4()),
        title=title,
        date=date,
        owner=owner,
    )

    meetings.append(meeting)

    logger.info(f"Meeting created with id {meeting.id}")

    return meeting


def list_meetings() -> list[Meeting]:
    logger.info("Listing meetings")
    return meetings