import { goto } from '$app/navigation';
import { redirect } from '@sveltejs/kit';

export function load({ cookies}) {
    cookies.delete("token", { path: "/" });
    cookies.delete("token_type", { path: "/" });
    throw redirect(302, '/'); 
}