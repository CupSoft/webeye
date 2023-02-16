import { configureStore } from '@reduxjs/toolkit'
import { api } from '../services/apiService/apiService'

const store = configureStore({
  reducer: {
    [api.reducerPath]: api.reducer
  },
  middleware: getDefaultMiddleware => getDefaultMiddleware().concat(api.middleware)
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch