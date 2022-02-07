var logs = []
var socket
var timeout
const methods = { // eslint-disable-line no-unused-vars
    chartConnect: () => {
        return new Promise((resolve, reject) => {
            socket = new WebSocket('ws://localhost:8000/ws')
            socket.onopen = () => {
                logs.push({event: 'connect complete: ', data: 'ws://localhost:8000/ws'})

                // socket.send("2017-08-17T13:00:00") // 초기값은 BaseChart에서 입력받고 send해주면 통신 시작되는 것으로 바꾸기
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

