<script>
	import {Alert, Card} from 'flowbite-svelte';
    let currentMessage = '';
    import { onMount } from 'svelte';
	import store from './store.js';
	import Message from './message.svelte';
	let message;
	let messages = [];

	onMount(() => {
		store.subscribe(currentMessage => {
            messages = [...messages, currentMessage];
		})
	})

	function onSendMessage() {
		 if (message.length > 0) {
			 store.sendMessage(message);
			 messages = [...messages, message];
			 message = "";

		 }
	}

	let chat_name = "main"
	import {ForwardSolid} from 'flowbite-svelte-icons';
	import {Listgroup} from 'flowbite-svelte';

	let buttons = [
		{name: 'Profile', mycustomfield: 'data1', current: true},
		{name: 'Settings', mycustomfield: 'data2'},
		{name: 'Messages', mycustomfield: 'data3'},
		{name: 'Download', mycustomfield: 'data4', disabled: true, attrs: {type: 'submit'}}
	];

</script>

<h1>Hello Chat</h1>

<input type="text" bind:value={message} />
<button on:click={onSendMessage}>
	<ForwardSolid class="w-6 h-6"/>
</button>


chat_name
<div class="flex w-full">
<Listgroup active items={buttons} let:item class="w-48" on:click={(e) => alert(Object.entries(e.detail))}>
  {item.name}
</Listgroup>

	<div class="justify-center w-full bg-gray-800">
		{#each messages as message, i}
			<Message {message} direction={i % 2 == 0 ? "left" :  "right" } jystify={i % 2 == 0 ? "start" :  "end" }
					 user={i % 2 == 0 ? "User" :  "Bot" }/>
		{/each}
	</div>
</div>
