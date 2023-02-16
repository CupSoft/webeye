import { createAction, createReducer } from "@reduxjs/toolkit";

const change = createAction<boolean, 'auth'>('auth')

export const isAuthReducer = createReducer(false, builder => {
  builder.addCase(
    change, 
    (state, action) => state = action.payload
    )
})