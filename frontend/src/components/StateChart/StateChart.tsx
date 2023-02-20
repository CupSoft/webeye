import React from 'react';
import { ResponsiveContainer, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line } from 'recharts';
import { StateChartPropsType } from './StateChartTypes';
import styles from './StateChart.module.scss'
import { useGetAllCheckResultsQuery } from '../../services/apiService/apiService';

const StateChart = ({sourceUuid}: StateChartPropsType) => {
  const {data, isLoading} = useGetAllCheckResultsQuery({max_count: 7, timedelta: 1, source_uuid: sourceUuid});

  if (isLoading) {
    return null
  }

  return (
    <ResponsiveContainer 
      className={styles.chart_container}
    >
        <LineChart
          data={data}
          margin={{
            top: 10,
            right: 30,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="datetime" stroke='#c5c5c5'/>
          <YAxis stroke='#c5c5c5'/>
          <Tooltip wrapperClassName={styles.chart_tooltip}/>
          <Legend />
          <Line type="linear" dataKey="ok" stroke="#00ff00" fill="#00ff00" />
          <Line type="linear" dataKey="partial" stroke="#ffff00" fill="#ffff00" />
          <Line type="linear" dataKey="critical" stroke="#ff0000" fill="#ff0000" />
        </LineChart>
      </ResponsiveContainer>
  );
};

export default StateChart;