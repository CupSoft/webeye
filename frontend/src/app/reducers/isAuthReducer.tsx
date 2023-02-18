import { createAction, createReducer } from "@reduxjs/toolkit";

const change = createAction<boolean, 'isAuth'>('isAuth')

export const isAuthReducer = createReducer(false, builder => {
  builder.addCase(
    change, 
    (state, action) => state = action.payload
    )
})