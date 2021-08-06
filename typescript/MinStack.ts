
class MinStack {
    private _stk: number[] = [];
    constructor() {}

    push(val: number): void {
        this._stk.push(val);
    }

    pop(): void {
        let _=this._stk.pop();
    }

    top(): number {
        return this._stk[this._stk.length - 1];
    }

    getMin(): number {
        let minNum: number = Number.POSITIVE_INFINITY;
        for (let index = 0; index < this._stk.length; index++) {
            minNum = Math.min(minNum, this._stk[index]);
        }
        return minNum;
    }
}
