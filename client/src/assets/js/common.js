var socket
var logs = []

const methods = { // eslint-disable-line no-unused-vars
    chartConnect: () => {
        socket = new WebSocket('ws://localhost:8000/ws')
        socket.onopen = () => {
            logs.push({event: 'connect complete: ', data: 'ws://localhost:8000/ws'})
            console.log(logs)
            setInterval(() => socket.send('echo'), 5000)
    
            socket.onmessage = ({data}) => {
                const recv = JSON.parse(data)
                const value = Math.floor((recv.value * 100))
                return value // 스토어로 값 보내기.
                
            }
        }
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
