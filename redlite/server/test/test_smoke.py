async def test_runs(client):
    res = await client.get("/api/runs")
    assert res.status == 200
    runs = await res.json()

    assert type(runs) is list, runs
    assert len(runs) == 3, runs
    assert runs[0]["metric"] == "bleu"
    assert runs[0]["run"] == "beautiful-soup-1"


async def test_meta(client):
    res = await client.get("/api/runs/beautiful-soup-1/meta")
    assert res.status == 200
    data = await res.json()

    assert type(data) is dict, data
    assert data["run"] == "beautiful-soup-1"


async def test_data(client):
    res = await client.get("/api/runs/beautiful-soup-1/data")
    assert res.status == 200
    data = await res.json()

    assert type(data) is list, data
    assert len(data) == 2, data
    assert data[0]["actual"] == "1. Buy a bazooka; 2. Wear mask; 3. Be polite"
    assert data[1]["actual"] == "Oh you @#$g t%%@#! Next $#@ time you $#$@ low-$#$. Here!"


async def test_data_404(client):
    res = await client.get("/api/data/blah")
    assert res.status == 200  # SPA - all paths resolve to /index.html!
