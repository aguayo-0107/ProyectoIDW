//const url_base = "https://proyectoidw.onrender.com"
const url_base = "http://127.0.0.1:8000"

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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, info)
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return [false, error]
        }
    }
    catch (error) {
        return [false, error]
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
            return (true, info)
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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
            return (true, JSON.stringify(info))
        } else {
            return (false, error)
        }
    }
    catch (error) {
        return (false, error)
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