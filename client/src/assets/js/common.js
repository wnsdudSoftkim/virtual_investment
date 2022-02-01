var logs = []
var socket
var interval
const methods = { // eslint-disable-line no-unused-vars
    chartConnect: () => {
        return new Promise((resolve, reject) => {
            socket = new WebSocket('ws://localhost:8000/ws')
            socket.onopen = () => {
                logs.push({event: 'connect complete: ', data: 'ws://localhost:8000/ws'})
                interval = setInterval(() => socket.send('echo'), 4000)
                resolve(socket)
                // socket.onmessage = ({data}) => {
                //     const recv = JSON.parse(data)
                //     const value = Math.floor((recv.value * 100))
                //     resolve(value)
                    
                // }
            }
            socket.onerror = (err) => {
                reject(err)
            }
        })
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

