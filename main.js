import { check } from "k6"
import http from "k6/http"

export let options = {
    vus: 200,
    duration: "5m"
}

export default function () {
    const id = Math.floor(Math.random() * 100_000) + 1

    const res = http.get(`http://localhost:8080/items/${id}`, {
        tags: { name: "GET /items/:id" }
    })

    check(res, {
        "status was 200": (r) => r.status === 200
    })
}
