import React from 'react';
import { useGetAllSourcesQuery } from '../../services/apiService/apiService';
import SourceCard from '../SourceBadge/SourceBadge';
import styles from './SourcesTable.module.scss'

const SourcesTable = ({limit=-1, skip=-1}) => {
  let params = {}
  if (limit !== -1) {
    params = {limit}
  }
  if (skip !== -1) {
    params = {...params, skip}
  }
  const {data: sources, isLoading} = useGetAllSourcesQuery(params)

  if (isLoading) {
    return null
  }
  
  return (
    <>
      {sources?.length ?
        <div className={styles.table}>
          {sources.map((source, i) => <SourceCard i={i} key={source.uuid} {...source}/>)}
        </div>
        : <span className={styles.no_resources}>В базе данных пока нет ресурсов</span>
      }
    </>
  );
};

export default SourcesTable;