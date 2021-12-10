const webpack = require('webpack');
const path = require('path');

module.exports = (env) => {
  //console.log(env);
  //const bundleName = (env.env === 'dev') ? '.js' : '.min.js';

  //path: path.join(__dirname, 'dist'),

  const bundleName = '.min.js';
  return {
    entry: {
      'admin': './src/admin.js',
      },
    output: {
      path: path.join(__dirname, '..', 'app/static/js'),
      filename: `[name]${bundleName}`,
    },
    plugins: [
      new webpack.DefinePlugin({
        REACT_ENV: JSON.stringify(env.env),
      }),
    ],
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader'
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader']
        }
      ],
    },
    //devtool: 'cheap-module-eval-source-map'
  }
};
