import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { redirect } from '@sveltejs/kit';

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const email = data.get('email');
        const password = data.get('password');
        
        const response = await fetch('http://'+process.env.SERVER_IP+':8080/user/signin', {
            method: 'POST',
            body: JSON.stringify({ "login": email, "email": email, "password": password }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.status == 200) {
            const text = await response.json();
            cookies.set('email',email, { path: '/' });
            cookies.set('token',text.access_token, { path: '/' });
            cookies.set('token_type',text.token_type, { path: '/' });
            throw redirect(302, '/'); 
        }
        if (response.status == 400) {
            return fail(400, { is_user: false, wrong_pass: false })
        }
        if (response.status == 401) {
            return fail(400, { is_user: true, wrong_pass: true, email: email })
        }
    }
} satisfies Actions;    