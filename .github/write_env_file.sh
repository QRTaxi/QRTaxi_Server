echo "SECRET_KEY=${{ secrets.SECRET_KEY }}" > .env
echo "DB_USER=${{ secrets.DB_USER }}" >> .env
echo "DB_NAME=${{ secrets.DB_NAME }}" >> .env
echo "DB_PASSWORD=${{ secrets.DB_PASSWORD }}" >> .env
echo "DB_HOST=${{ secrets.DB_HOST }}" >> .env
echo "DB_PORT=${{ secrets.DB_PORT }}" >> .env