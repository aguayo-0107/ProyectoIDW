const url_base = "https://proyectoidw.onrender.com"

//CONCIERTOS
//Post /conciertos

async function postConcierto(data) {
    try {
        const response = await fetch(url_base + "/conciertos" , {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Get /conciertos (lugar | None)

async function getConciertos(data) {
    try {
        const response = await fetch(url_base + "/conciertos", {
            method: "GET",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Get /conciertos/id

async function getConcierto(id) {
    try {
        const response = await fetch(url_base + "/conciertos/" + id, {
            method: "GET",
            headers: {"Content-Type": "application/json"}
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Patch /conciertos/id (nueva fecha)

async function patchConcierto(id, data) {
    try {
        const response = await fetch(url_base + "/conciertos/" + id , {
            method: "PATCH",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Delete /concierto/id

async function deleteConcierto(id) {
    try {
        const response = await fetch(url_base + "/concierto/" + id, {
            method: "DELETE",
            headers: {"Content-Type": "application/json"}
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}


//ARTISTAS
//Post /artistas

async function postArtista(data) {
    try {
        const response = await fetch(url_base + "/artistas" , {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Get /artistas (nombre | None)

async function getArtistas(data) {
    try {
        const response = await fetch(url_base + "/artistas", {
            method: "GET",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Get /artistas/id

async function getArtista(id) {
    try {
        const response = await fetch(url_base + "/artistas/" + id, {
            method: "GET",
            headers: {"Content-Type": "application/json"}
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Patch /artistas/id (nuevo genero)

async function patchArtista(id, data) {
    try {
        const response = await fetch(url_base + "/artistas/" + id , {
            method: "PATCH",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

//Delete /artista/id

async function deleteArtista(id) {
    try {
        const response = await fetch(url_base + "/artista/" + id, {
            method: "DELETE",
            headers: {"Content-Type": "application/json"}
        })
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            const info = await response.text()
            return [false, JSON.parse(info).detail[0].msg ?? JSON.parse(info).detail]
        }
    }
    catch (error) {
        return [false, error.message]
    }
}

async function getLista(page, size) {
    try {
        const response = await fetch(`${url_base}/listaArtistas?page=${page}&size=${size}`);
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            return [false, error]
        }
    }
    catch (error) {
        return [false, error]
    }
}

async function getListaC(page, size) {
    try {
        const response = await fetch(`${url_base}/listaConciertos?page=${page}&size=${size}`);
        if (response.ok) {
            const info = await response.json()
            return [true, info]
        } else {
            return [false, error]
        }
    }
    catch (error) {
        return [false, error]
    }
}