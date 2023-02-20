import { CartesianGrid, Legend, Bar, BarChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { useGetAllCheckResultsQuery } from '../../services/apiService/apiService';
import styles from './StateChart.module.scss';
import { StateChartPropsType } from './StateChartTypes';

const StateChart = ({sourceUuid}: StateChartPropsType) => {
  const {data, isLoading} = useGetAllCheckResultsQuery({max_count: 10, timedelta: 86000, source_uuid: sourceUuid});

  if (isLoading) {
    return null
  }

  return (
    <ResponsiveContainer 
      className={styles.chart_container}
    >
        <BarChart
          data={data}
          margin={{
            top: 10,
            right: 30,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="end_datetime" stroke='#c5c5c5'/>
          <YAxis stroke='#c5c5c5'/>
          <Tooltip wrapperClassName={styles.chart_tooltip}/>
          <Legend />
          <Bar type="linear" dataKey="ok" stackId='1' stroke="#00ff00" fill="#00ff00" />
          <Bar type="monotone" dataKey="partial" stackId='1' stroke="#ffff00" fill="#ffff00" />
          <Bar type="monotone" dataKey="critical" stackId='1' stroke="#ff0000" fill="#ff0000" />
        </BarChart>
      </ResponsiveContainer>
  );
};

export default StateChart;