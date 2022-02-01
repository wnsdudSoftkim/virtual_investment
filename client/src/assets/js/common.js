var socket
var logs = []

const methods = { // eslint-disable-line no-unused-vars
    chartConnect: async() => {
        return new Promise((resolve, reject) => {
            socket = new WebSocket('ws://localhost:8000/ws')
            socket.onopen = () => {
                logs.push({event: 'connect complete: ', data: 'ws://localhost:8000/ws'})
                setInterval(() => socket.send('echo'), 5000)
        
                socket.onmessage = ({data}) => {
                    const recv = JSON.parse(data)
                    const value = Math.floor((recv.value * 100))
                    resolve(value)
                    
                }
            }
            socket.onerror = (err) => {
                reject(err)
            }
        })
    },
    chartDisconnect: () => {
        socket.close()
        logs = []
    }
}

export default methods
// export default {
//     install (Vue) {
//         Vue.prototype.$chartConnect = methods.chartConnect
//         Vue.prototype.$chartDisconnet = methods.chartDisconnect
//     }
// }
