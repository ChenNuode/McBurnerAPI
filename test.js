fetch("http://127.0.0.1:5000/sendmefood/1,2")
	.then(res => res.json())
	.then(console.log(data))