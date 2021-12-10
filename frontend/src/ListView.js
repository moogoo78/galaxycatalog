import * as React from 'react';
import {useEffect, useState} from 'react';

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
//import RadioButtonUncheckedIcon from '@mui/icons-material/RadioButtonUnchecked';
//import RadioButtonCheckedIcon from '@mui/icons-material/RadioButtonChecked';
import CheckIcon from '@mui/icons-material/Check';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/system';

import { Link as RouterLink, Outlet } from "react-router-dom";

const API_PREFIX = '/admin/api/';


const TableWrapper = styled('div')`
  th {
    background-color: #eee;
  }
`;

const DataContent = ({result}) => {
  return result.rows.map((row) => {
    const cellList = result.header.map((column, i) => {
      // each cell
      const cellAlign = (column[2] && column[2].align !== '') ? column[2].align : null;
      let cellValue = row[column[0]];
      if (column[2] && column[2].type == 'x_field_number') {
        const fieldNumbers = [];
        for (let i in cellValue) {
          if (cellValue[i].length > 0) {
            fieldNumbers.push(<div key={i}>{cellValue[i][0]}<Typography variant="h5" style={{fontweight:'bold'}}>{cellValue[i][1]}</Typography></div>);
          }
        }
        cellValue = <>{fieldNumbers.map((x)=>x)}</>;
      } else if (column[2] && column[2].type == 'radio') {
        cellValue = (cellValue === true) ? <CheckIcon /> : null;
      }

      if (i === 0) {
        // row index
        return (
            <TableCell component="th" scope="row" key={i} align={cellAlign}>
            <RouterLink to={`/admin/${result.model}/${row.pk}/edit`}>{cellValue}</RouterLink>
            </TableCell>
        );
      } else {
        return (
            <TableCell  key={i} align={cellAlign}>
            {cellValue}
          </TableCell>
        );
      }
    });
    return (
      <TableRow
      key={row.pk}
      sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
      hover={true}
      >
       {cellList}
      </TableRow>
      )
  });
}

export default function ListView(props) {
  const [isLoading, setIsLoading] = useState(true);
  const [result, setResult] = useState(null);
  const {model} = props;
  const api_url = `${API_PREFIX}${model}`;
  //console.log(api_url)
  useEffect(() => {
    setIsLoading(true);

    fetch(api_url)
      .then((resp)=>resp.json())
      .then((data)=>{
        //console.log(jsonData);
        setResult(data);
        setIsLoading(false);
      });
  }, [model]);

  //console.log(result, isLoading);
  if (isLoading) {
    return <h1>Loading...</h1>;
  } else {
    return (
      <TableWrapper>
      <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
      <TableHead>
      <TableRow>
      {result.header.map((v, i) =>
        <TableCell key={i} align={(v[2] && v[2].align !== '') ? v[2].align : null}>{v[1]}</TableCell>
      )}
      </TableRow>
      </TableHead>
      <TableBody>
        <DataContent result={result} />
      </TableBody>
      </Table>
        </TableContainer>
         <Outlet />
      </TableWrapper>
    )
  }
}
