import { writable } from 'svelte/store';

const messageStore = writable('');

// @ts-ignore
const socket = new WebSocket('ws://'+process.env.SERVER_IP+':8080/ws/messages');

// Connection opened
socket.addEventListener('open', function (event) {
    console.log("It's open");
});

// // Listen for messages
// socket.addEventListener('message', function (event) {
//     messageStore.set(event.data);
// });

socket.onmessage = function(event) {
  messageStore.set(event.data);
};

const sendMessage = (message) => {
	if (socket.readyState <= 1) {
		socket.send(message);
	}
}


export default {
	subscribe: messageStore.subscribe,
	sendMessage
}
