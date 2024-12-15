


dotenv.load_dotenv(Path('.env'))  # {...}


client = MongoClient(
os.environ.get('MONGO_URI'),
    tls=True,  # Использование TLS (SSL)
    tlsAllowInvalidCertificates=True
)


db = client.get_database(
    name=os.environ.get('TARGET_DB'),
    write_concern=WriteConcern(w="majority")
) # use db

collection = db.get_collection(
    name=os.environ.get('TARGET_COLLECTION'),
    write_concern=WriteConcern(w="majority"),
    read_preference=ReadPreference.PRIMARY
)


session: ClientSession = client.start_session()


with session.start_transaction():
    try:
        collection.update_one(
            {"name": "Elena"},
            {"$inc": {"money": -90}},
            session=session
        )

        elena = collection.find_one(
            {"name": "Elena"},
            session=session
        )

        if elena['money'] < 0:
            raise ValueError("Balance cannot be negative")

        collection.update_one(
            {"name": "Admin"},
            {"$inc": {"money": 90}},
            session=session
        )

    except (PyMongoError, ValueError) as e:
        print(f"ERROR, transaction will be aborted: [{e}]")
        session.abort_transaction()
    else:
        session.commit_transaction()
    finally:
        session.end_session()
        client.close()





