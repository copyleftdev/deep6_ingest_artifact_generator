from neo4j import GraphDatabase
import hashlib
import uuid


driver = GraphDatabase.driver("bolt://neo1.qa1.deep6.ai:7687", auth=("neo4j", "Sk3Iy8TEuqEOnzPM3Otg"))


def hash_pass(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


def account_creation(
    adminUser, uuid, firstName, lastName, displayName, username, password
):
    pl = """MERGE (u:Account  { uuid: %s }) ON CREATE SET u.remote = false
          SET u:User, u.username = %s
          SET u.hashedPassword = %s, u.firstName = %s, u.lastName=%s, u.displayName=%s
          SET u :Deep6Operations:Deep6Researcher
          RETURN u.username AS username, labels(u) AS roles, u.uuid AS uuid, u.remote AS remote""" % (
        uuid,
        username,
        hash_pass(password),
        firstName,
        lastName,
        displayName,
    )
    db = driver.session()
    results = db.run(pl)
    print(results)


# ac = account_creation(
#     "sampleAdmin", "long_uuis", "Don", "Johnson", "djohnson", "dman", "pass"
# )


sample_user = '''
match(n:DataElement) return n limit 1000
'''

db = driver.session()

results = db.run(sample_user)

print(results.values())
