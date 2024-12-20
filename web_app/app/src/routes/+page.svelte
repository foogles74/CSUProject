<script>
	import {Alert, Card, Input} from 'flowbite-svelte';
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

	let chat_name = "Main"
	import {ForwardSolid} from 'flowbite-svelte-icons';
	import {Listgroup} from 'flowbite-svelte';

	let buttons = [
		{name: 'Main'},
		{name: 'Settings'},
		{name: 'Messages'},
		{name: 'Download'}
	];

</script>

<div class="flex w-full h-full">
	<div class="flex-none mt-10 ml-10">
		<h3 class="p-1 text-center text-xl font-medium text-gray-900 dark:text-white">{chat_name}</h3>
		<Listgroup active items={buttons} let:item class="w-48" on:click={(e) => chat_name = e.detail["name"]}>
			{item.name}
		</Listgroup>
	</div>

	<div class="grow bg-gray-600 mt-10 mx-10">
		<div class="overflow-y-auto" style="max-height: 80dvh; min-height: 80vh;">
			{#each messages as message, i}
				<Message {message} direction={i % 2 == 0 ? "left" :  "right" } jystify={i % 2 == 0 ? "start" :  "end" }
						 user={i % 2 == 0 ? "User" :  "Bot" }/>
			{/each}
		</div>

		<form class="flex w-full" on:keydown={(event) => event.key != 'Enter'}>
			<Input class="grow dark:text-white " type="text" size="sm" placeholder="Сообщение"
				   bind:value={message}/>
			<button class="flex-none" on:click={onSendMessage} on:keypress={(e)=>alert(e)}>
				<ForwardSolid class="w-6 h-6 justify-end"/>
			</button>
		</form>

	</div>
</div>
