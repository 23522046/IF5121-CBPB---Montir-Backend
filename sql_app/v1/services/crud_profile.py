from sqlalchemy.orm import Session
from sql_app.v1 import schemas
from sql_app.v1 import models

def create_profile(db: Session, profile: schemas.Profil):
    db_profil = models.Profil(id_user=profile.id_user, nama=profile.nama, alamat=profile.alamat, telepon=profile.telepon, picture=profile.picture)
    db.add(db_profil)
    db.commit()
    db.refresh(db_profil)
    return db_profil