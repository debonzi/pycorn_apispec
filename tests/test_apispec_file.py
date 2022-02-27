def test_dummy(testapp):
    resp = testapp.post_json("/api/v1/users", {"username": "tester001"})
    assert resp.json == [{"username": "tester001"}]
