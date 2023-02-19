import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { RootState } from '../../app/store'
import { SocialReportsGetTypes, SourceGetTypes, UserLoginResponseTypes, UserRegistrRequestTypes, UserRegistrResponseTypes } from './apiServiceTypes'

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_LINK,
    prepareHeaders(headers, {getState}) {
      const token = localStorage.getItem('token')

      if (token) {
        headers.set('Authorization', token)
      }

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
    checkUser: builder.mutation<UserRegistrResponseTypes, void>({
      query: () => ({url: '/auth/users/me'})
    }),
    getSource: builder.query<SourceGetTypes, string>({
      query: (uuid) => ({ url: `resources/${uuid}` })
    }),
    getAllSources: builder.query<SourceGetTypes[], void>({
      query: () => ({ url: `resources`})
    }),
    getAllSocialReports: builder.query<SocialReportsGetTypes[], void>({
      query: () => ({ url: 'social_reports'})
    })
  })
})

export const { useRegisterUserMutation } = api
export const { useLoginUserMutation } = api
export const { useGetAllSourcesQuery } = api
export const { useGetSourceQuery } = api
export const { useCheckUserMutation } = api
export const { useGetAllSocialReportsQuery } = api