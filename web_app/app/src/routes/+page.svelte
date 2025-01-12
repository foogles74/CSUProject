<script lang="ts">
	import {Input} from 'flowbite-svelte';
	import {ForwardSolid} from 'flowbite-svelte-icons';
	import {Listgroup} from 'flowbite-svelte';
	import Message from './message.svelte';
	import type { PageData , ActionData } from './$types';
	import { enhance, applyAction } from '$app/forms';
	let { data, form }: { data: PageData, form: ActionData} = $props();
	let messages = [];
	messages = data.messages
	let message;
	import type { ActionResult } from '@sveltejs/kit';
	import { deserialize } from '$app/forms';
	import { invalidateAll, goto } from '$app/navigation';

	let chat_name = "Первый Чат"
	let visible = true
	let buttons = [
		{name: 'Первый Чат'},
		{name: 'Второй Чат'},
		{name: 'Третий Чат'},
		{name: 'Четвертый Чат'}
	];

	async function handleSubmit(event: SubmitEvent & { currentTarget: EventTarget & HTMLFormElement}) {
		event.preventDefault();
		const data = new FormData(event.currentTarget);
		console.log("start")
		visible = false
		const response = await fetch(event.currentTarget.action, {
			method: 'POST',
			body: data
		});

		const result: ActionResult = deserialize(await response.text());

		if (result.type === 'success') {
			// rerun all `load` functions, following the successful update
			visible = true
			await invalidateAll();
		}

		applyAction(result);
	}
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

		<form method="POST" class="flex w-full" onsubmit={handleSubmit}
			  use:enhance={({ formElement, formData, action, cancel }) => {
				    visible = false
				    messages = [...messages, message]
					message = ""
					return async ({ result }) => {
						messages = [...messages, result.data.otvet.toString()]
						visible = true
						};
		}

		}>
			{#if visible === true}
				<Input class="grow dark:text-white " type="text" size="sm" placeholder="Сообщение" name="message"
					   bind:value={message}/>
				<Input class="grow dark:text-white hidden" type="text" size="sm" placeholder="Сообщение" name="chat_name"
					   bind:value={chat_name}/>
				<button class="flex-none">
					<ForwardSolid class="w-6 h-6 justify-end"/>
				</button>
			{/if}
		</form>

	</div>
</div>
