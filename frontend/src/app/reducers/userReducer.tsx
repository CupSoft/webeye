import { createAction, createReducer } from "@reduxjs/toolkit";
import { UserStoreTypes } from "../../services/apiService/apiServiceTypes";

const changeUser = createAction<UserStoreTypes, 'changeUser'>('changeUser')

export const userReducer = createReducer({
    isAdmin: false,
    isAuth: false,
    email: '',
    uuid: ''
}, builder => {
  builder.addCase(
    changeUser,
    (state, action) => ({...state, ...action.payload})
  )
})