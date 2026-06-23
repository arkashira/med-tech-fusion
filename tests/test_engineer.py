from engineer import Engineer, EngineerPlatform

def test_add_engineer():
    platform = EngineerPlatform()
    engineer = Engineer(1, "John Doe", ["Project 1", "Project 2"], 5)
    platform.add_engineer(engineer)
    assert platform.get_engineer_profile(1) == engineer

def test_search_engineers():
    platform = EngineerPlatform()
    engineer1 = Engineer(1, "John Doe", ["Project 1", "Project 2"], 5)
    engineer2 = Engineer(2, "Jane Doe", ["Project 3", "Project 4"], 3)
    platform.add_engineer(engineer1)
    platform.add_engineer(engineer2)
    results = platform.search_engineers("Doe")
    assert len(results) == 2
    assert engineer1 in results
    assert engineer2 in results

def test_get_engineer_profile():
    platform = EngineerPlatform()
    engineer = Engineer(1, "John Doe", ["Project 1", "Project 2"], 5)
    platform.add_engineer(engineer)
    assert platform.get_engineer_profile(1) == engineer
    assert platform.get_engineer_profile(2) is None

def test_send_message():
    platform = EngineerPlatform()
    engineer = Engineer(1, "John Doe", ["Project 1", "Project 2"], 5)
    platform.add_engineer(engineer)
    assert platform.send_message(1, "Hello, engineer!") is True
    assert platform.send_message(2, "Hello, engineer!") is False
