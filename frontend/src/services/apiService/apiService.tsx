import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { SourceDataTypes, UserDataTypes } from './apiServiceTypes'

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_LINK,
    prepareHeaders(headers) {
      return headers
    }
  }),
  tagTypes: ['User', 'Source'],
  endpoints: (builder) => ({
    postUser: builder.mutation<UserDataTypes, UserDataTypes>({
      query: (user) => ({
        method: 'POST',
        url: 'registration',
        body: JSON.stringify(user),
        headers: {'Content-Type': 'application/json'}
      })
    }),
    getSource: builder.mutation<string, string>({
      query: (id) => ({ url: `source/${id}` })
    }),
    getAllSources: builder.mutation<SourceDataTypes[], string>({
      query: () => ({ url: `sources`})
    })
  })
})

export const { usePostUserMutation } = api
export const { useGetSourceMutation } = api
export const { useGetAllSourcesMutation } = api