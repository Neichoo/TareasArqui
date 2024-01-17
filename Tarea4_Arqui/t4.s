    .data
f: .word 2
n: .word 2
x: .word 2

    .text
landing:
	ldr r0, =n
	ldr r0,[r0]
	ldr r3, =f
	ldr r3, [r3]
	cmp r3, #1
	beq main_f1
main_f1:
	ldr r1, =x
	ldr r1,[r1]
	b fuumo

main_f2:
	b aureo

fuumo:
	cmp r0,#0
        beq if_fuumo
        cmp r0,#1
        beq elif_fuumo
        b else_fuumo

if_fuumo:
        add r2,r2,#1
        mov pc,lr
elif_fuumo:
        add r2,r2,r1
        add r2,r2,r1
        mov pc,lr

else_fuumo:
        sub r0,r0,#1
        push {r0}
        bl fuumo
        pop {r0}
        sub r0,r0,#1
        bl fuumo
        pop {r0}
        cmp r0,#0
        beq fin
        bl else_lucas
        mov pc,lr

lucas:
        cmp r0,#0
        beq if_lucas
        cmp r0,#1
        beq elif_lucas 
        b else_lucas

if_lucas:
        add r2,r2,#2
        mov pc,lr

elif_lucas:
        add r2,r2,#1
        mov pc,lr

else_lucas:
        sub r0,r0,#1
        push {r0}
        bl lucas
        pop {r0}
        sub r0,r0,#1
        bl lucas
        pop {r0}
        cmp r0,#0
        beq fin
        bl else_lucas
        mov pc,lr

fibonacci:
        cmp r0,#0
        beq if_fibonacci
        cmp r0,#1
        beq elif_fibonacci
        b else_fibonacci

if_fibonacci:
        add r2,r2,#0
        mov pc,lr

elif_fibonacci:
        add r2,r2,#1
        mov pc,lr

else_fibonacci:
        sub r0,r0,#1
        push {r0}
        bl fibonacci
        pop {r0}
        sub r0,r0,#1
        bl fibonacci
        pop {r0}
        cmp r0,#0
        beq fin
        bl else_fibonacci
        mov pc,lr
aureo:
	bl lucas
	bl fibonacci
	b fin

fin:
        mov r0,#0
        bl printInt
        wfi
