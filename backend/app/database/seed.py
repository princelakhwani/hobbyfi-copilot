from datetime import date, datetime, timedelta

from app.database.base import Base
from app.database.session import SessionLocal, engine
from app.models.vendor import Vendor
from app.models.sport import Sport
from app.models.user import User
from app.models.membership import Membership
from app.models.booking import Booking
from app.models.payment import Payment


def seed():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Prevent duplicate seeding
    if db.query(Vendor).first():
        print("Database already seeded.")
        db.close()
        return

    vendor = Vendor(
        name="SmashZone Sports Academy",
        email="owner@smashzone.com",
        phone="9999999999",
        city="Jaipur",
    )

    db.add(vendor)
    db.flush()

    badminton = Sport(
        vendor_id=vendor.id,
        name="Badminton",
        description="Indoor badminton coaching",
    )

    tennis = Sport(
        vendor_id=vendor.id,
        name="Tennis",
        description="Professional tennis coaching",
    )

    db.add_all([badminton, tennis])
    db.flush()

    rahul = User(
        vendor_id=vendor.id,
        sport_id=badminton.id,
        name="Rahul Sharma",
        email="rahul@test.com",
        phone="9876543210",
        trial_remaining=2,
    )

    priya = User(
        vendor_id=vendor.id,
        sport_id=tennis.id,
        name="Priya Patel",
        email="priya@test.com",
        phone="9876543211",
        trial_remaining=0,
    )

    db.add_all([rahul, priya])
    db.flush()

    membership = Membership(
        user_id=rahul.id,
        plan_name="Gold",
        start_date=date.today(),
        expiry_date=date.today() + timedelta(days=30),
        status="ACTIVE",
    )

    db.add(membership)
    db.flush()

    booking = Booking(
        vendor_id=vendor.id,
        user_id=rahul.id,
        booking_date=datetime.now(),
        amount=1200,
        status="BOOKED",
    )

    db.add(booking)
    db.flush()

    payment = Payment(
        booking_id=booking.id,
        amount=1200,
        payment_method="UPI",
        status="SUCCESS",
    )

    db.add(payment)

    db.commit()
    db.close()

    print("✅ HobbyFi demo data inserted.")


if __name__ == "__main__":
    seed()