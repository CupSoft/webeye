import { SerializedError } from "@reduxjs/toolkit";
import { FetchBaseQueryError } from "@reduxjs/toolkit/dist/query";
import { NavigateFunction } from "react-router-dom";
import { AppDispatch } from "../app/store";
import { UserLoginResponseTypes } from "../services/apiService/apiServiceTypes";
import { MAIN_ROUTE } from "./constants";

export const handleLoginUser = (dispatch: AppDispatch, navigate: NavigateFunction, params: URLSearchParams, setAuthError: React.Dispatch<React.SetStateAction<string>>) => (value: { data: UserLoginResponseTypes; } | { error: FetchBaseQueryError | SerializedError; }) => {
  if ('error' in value) {
    setAuthError('Введен неверный email или пароль')
    return
  }

  const {access_token, token_type} = value.data

  localStorage.setItem('token', `${token_type} ${access_token}`)
  
  dispatch({
    type: 'changeUser', 
    payload: {
      isAuth: true
    }
  })
  
  navigate(params?.get('next_page') ?? MAIN_ROUTE)
}