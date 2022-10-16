let input=prompt("what would you like you do")
const todos =['collect eggs','collect chick'];
while(input!=='quit' && input !=='q'){
    if(input==='list'){
        console.log('********')
        for(let i=0;i<todos.length;i++){
            console.log(`${i}: ${todos[i]}`);
        }
        console.log('********')
    }else if(input==='new'){
        const newTodo=prompt('ok,what to add?')
        todos.push(newTodo);
        console.log(`${newTodo} is added to the queue`);
    }else if(input==='delete'){
        const index=prompt("enter the index to delete")
       const deleted= todos.splice(index,1);
        console.log(`ok you deleted ${deleted[0]}`)
    }
    input=prompt("what would you like you do")


}
console.log("okay.you quit the app");
