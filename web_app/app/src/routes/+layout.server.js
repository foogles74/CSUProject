export async function load({ cookies }) {
	const auth = cookies.get('token');
    if (auth === undefined){
        cookies.delete("token", {path: "/"});
        cookies.delete("token_type", {path: "/"});
        cookies.delete("email", {path: "/"});
        return {
            auth: false,
            balance: 0
        };  
    }
    try {
        // @ts-ignore
        const response = await fetch('http://'+process.env.SERVER_IP+':8080/user/validate', {
            method: 'POST',
            body: JSON.stringify({"token": auth}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const response_balance = await fetch('http://'+process.env.SERVER_IP+':8080/balance/get_balance_route', {
            method: 'POST',
            body: JSON.stringify({"email": cookies.get('email')}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.status === 200 && response_balance.status === 200) {
            let balnce = await response_balance.json()
            return {
                auth: true,
                balance: balnce["balance"]
            };
        } else {
            cookies.delete("token", {path: "/"});
            cookies.delete("token_type", {path: "/"});
            cookies.delete("email", {path: "/"});
            return {
                auth: false,
                balance: 0
            };
        }
    } catch (e) {
        cookies.delete("token", {path: "/"});
        cookies.delete("token_type", {path: "/"});
        cookies.delete("email", {path: "/"});
        return {
                auth: false,
                balance: 0
            };
    }
}