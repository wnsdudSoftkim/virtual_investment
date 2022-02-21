var logs = []
var socket
var timeout
const methods = { // eslint-disable-line no-unused-vars
    chartConnect: () => {
        return new Promise((resolve, reject) => {
            socket = new WebSocket('wss://sheltered-chamber-00843.herokuapp.com/ws')
            // socket = new WebSocket('ws://localhost:8000/ws')
            socket.onopen = () => {
                logs.push({event: 'connect complete: ', data: 'ws://https://sheltered-chamber-00843.herokuapp.com/ws'})
                resolve(socket)
            }
            socket.onerror = (err) => {
                reject(err)
            }
        })
    },
    sendMessage:(message) => {
        clearTimeout(timeout)
        if (message === 1) {
            socket.send(JSON.stringify({'date':'1'}))
        }
        else {
            timeout = setTimeout(()=> socket.send(JSON.stringify({'date': message})),2000)
        }
        logs.push({event: 'send message: ', data: message})

    },
    sendTempMessage:(message) => {
        socket.send(message)
    },
    chartDisconnect: () => {
        socket.close()
        console.log('Connection close')
        logs = []
    }
}

export default methods

