import { createAction, createReducer } from "@reduxjs/toolkit";

const change = createAction<string, 'authToken'>('authToken')

export const authTokenReducer = createReducer('', builder => {
  builder.addCase(
    change,
    (state, action) => state = action.payload
  )
})