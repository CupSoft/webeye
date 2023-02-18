import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { SourceDataTypes, SourceGetTypes, UserLoginRequestTypes, UserLoginResponseTypes, UserRegistrRequestTypes, UserRegistrResponseTypes } from './apiServiceTypes'

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_LINK,
    prepareHeaders(headers) {
      headers.set('Authorization', localStorage.getItem('token_type') ?? '' + localStorage.getItem('access_token' ?? ''))
      return headers
    }
  }),
  tagTypes: ['User', 'Source'],
  endpoints: (builder) => ({
    registerUser: builder.mutation<UserRegistrResponseTypes, UserRegistrRequestTypes>({
      query: (user) => ({
        method: 'POST',
        url: 'auth/users',
        body: JSON.stringify(user),
        headers: {'Content-Type': 'application/json'}
      })
    }),
    loginUser: builder.mutation<UserLoginResponseTypes, FormData>({
      query: (user) => ({
        method: 'POST',
        url: 'auth/login/access-token',
        body: user,
        headers: {'Content-Type': undefined}
      })
    }),
    getSource: builder.mutation<SourceGetTypes, string>({
      query: (uuid) => ({ url: `resources/${uuid}` })
    }),
    getAllSources: builder.mutation<SourceDataTypes[], void>({
      query: () => ({ url: `resources`})
    })
  })
})

export const { useRegisterUserMutation } = api
export const { useLoginUserMutation } = api
export const { useGetAllSourcesMutation } = api
export const { useGetSourceMutation } = api