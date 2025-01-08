/**
 * @param {any} message
 * @param {any} chat_name
 */
async function SendMessage(message,chat_name) {
		// @ts-ignore
		const response = await fetch('http://' + process.env.SERVER_IP + ':8080/request_model', {
			method: 'POST',
			body: JSON.stringify({"text": message, "user": "foogles74", "chat_name": chat_name}),
			headers: {
				'Content-Type': 'application/json'
			}
		});
		console.log(response.json())
		if (response.status === 200) {
			console.log(response.json())
            return response.json()
		}
}

export default {
	SendMessage
}