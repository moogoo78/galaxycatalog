import * as React from 'react';
import {useEffect, useState} from 'react';

import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Toolbar from '@mui/material/Toolbar';
import Paper from '@mui/material/Paper';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Button from '@mui/material/Button';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Autocomplete from '@mui/material/Autocomplete';

import {Link as RouterLink, useParams} from 'react-router-dom';

import UnitCard from './UnitCard.js';

const API_PREFIX = '/admin/api/';


const FormElement = ({data}) => {
  //console.log(data);
  const key = data[0];
  const label = data[1];
  const type = data[2];
  const value = data[3];
  const options = (data[4] && data[4].options) ? data[4].options : null;
  console.log(value);
  if (type === 'text') {
    return (
      <TextField
      id={key}
      name={key}
      label={label}
      value={value}
      fullWidth
      variant="standard"
        />
    )
  } else if (type === 'x_collector'){
    /*
      onInputChange={(event: object, value: string, reason: string) => {
        if (reason === 'input') {
          changeOptionBaseOnValue(value);
        }
      }}

      groupBy={(option) => option.sec}
      freeSolo
      getOptionSelected={(option, value) => option.pk === value.id}
      renderOption={(props, option) => [props, option]}
      getOptionLabel={(option) => option.label}
    */
    return (
      <Autocomplete
      freesolo="true"
      id={key}
      groupBy={(option) => option.label[0]}
      options={options}
      renderInput={(params) => (
          <TextField {...params} label={label} variant="standard" name={key}/>
      )}
      />
    )
  } else if (type === 'x_units'){
    const unitList = value.map((unit)=>{
      return (<UnitCard key={key} />)
    });
    return (<>{unitList}</>)
  } else {
    return (
        <TextField
      id={key}
      name={key}
      label={label}
      fullWidth
      variant="standard"
        />
    )
  }
}

const FormContent = ({result}) => {
  return result.form.map((row) => {
    const gridSM = 12 / row.length;
    const rowElements = row.map((ele, ei) => {
      return (<Grid item xs={12} sm={gridSM} key={ei}><FormElement data={ele}/></Grid>)
    });
    return rowElements;
  });
}


export default function FormView(props) {
  const params = useParams();
  const itemId = params.itemId;
  const [result, setResult] = useState(null);
  const {model} = props;
  const api_url = `${API_PREFIX}${model}/${itemId}/form`;
  //console.log(params, props);
    useEffect(() => {
    fetch(api_url)
      .then((resp)=>resp.json())
      .then((data)=>{
        console.log(data);
        setResult(data);
      });
    }, [model, itemId]);

  //console.log(result);
  return (
      <>
      {(result !== null) ?
      <Container component="main" maxWidth="sm" sx={{ mb: 4 }}>
      <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
      <Breadcrumbs aria-label="breadcrumb">
        <Link underline="hover" color="inherit" component={RouterLink} to="/admin">
          admin
        </Link>
        <Link
          underline="hover"
          color="inherit"
          to={`/admin/${model}`}
          component={RouterLink}
        >
        {props.label}
        </Link>
        <Typography color="text.primary">{params.itemId}</Typography>
      </Breadcrumbs>
      <Typography component="h1" variant="h4" align="center">
      {props.label}
      </Typography>

      {/*<Typography variant="h6" gutterBottom>
        Shipping address
      </Typography>
       */}
       <Grid container spacing={3}>
       <FormContent result={result} />
       </Grid>
      </Paper>
      </Container>
       : null }
    </>
  );
}
