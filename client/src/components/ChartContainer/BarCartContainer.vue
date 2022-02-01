<template>
  <div class="container">
    <bar-chart
      v-if="loaded"
      v-bind:cbvalue="cbvalue"/>
  </div>
</template>

<script>
import BarChart from '@/components/Chart/BarChart'

export default {
    name: 'BarChartContainer',
    components: { BarChart },
    data: function(){
        return {
            loaded: false,
            logs:[],
            cbvalue: [90, 10, 20, 30, 50, 10, 30, 40, 60, 100, 20 , 40],
            status:'disconnected',
        }
    }, 
    mounted () {
        this.connect()
        try {
            this.loaded = true
        }catch(e) {
            console.log(e)
        }
    },
    computed: {
        comdata() {
            return this.cbvalue
        }
    },
    methods: {
        connect() {
            // const ws = new WebSocket('ws://localhost:8000/ws')
            // ws.onopen = () => {
            //     this.status = 'connected'
            //     console.log('status:  '+ this.status)
            //     this.logs.push({event: 'connect complete: ', data: 'ws://localhost:8000/ws'})

            //     setInterval(() => ws.send('echo'), 5000)

            //     ws.onmessage = ({data}) => {
            //         const recv = JSON.parse(data)
            //         const value = Math.floor((recv.value * 100))
            //         console.log(value)
            //         this.cbvalue = value
            //         // const copied = this.cbvalue.slice()
            //         // copied.push(value)
            //         // this.cbvalue = copied
            //         this.$forceUpdate()
                    
            //     }
            // }
        },
        disconnect() {
            // this.socket.close()
            // this.status = 'disconnected'
            // this.logs = []
        }
    }
}
</script>