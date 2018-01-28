#!/bin/bash
npm run build
aws s3 sync ./dist/ s3://www.activestock.us
