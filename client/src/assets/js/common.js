var logs = []
var socket
var interval
const methods = { // eslint-disable-line no-unused-vars
    chartConnect: () => {
        return new Promise((resolve, reject) => {
            socket = new WebSocket('ws://localhost:8000/ws')
            socket.onopen = () => {
                logs.push({event: 'connect complete: ', data: 'ws://localhost:8000/ws'})

                socket.send("2017-08-17T13:00:00") // 초기값은 BaseChart에서 입력받고 send해주면 통신 시작되는 것으로 바꾸기
                resolve(socket)
            }
            socket.onerror = (err) => {
                reject(err)
            }
        })
    },
    sendMessage:(message) => {
        if (message === 1) {
            socket.send(1)
        }
        else {
            setTimeout(()=> socket.send(message),2000)
        }
        logs.push({event: 'send message: ', data: message})

    },
    chartDisconnect: () => {
        socket.onclose = function () {
            clearInterval(interval);
          };
        socket.close()
        console.log('Connection close')
        logs = []
    }
}

export default methods

