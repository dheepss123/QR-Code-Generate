import qrcode
import cherrypy
import io

class QRGenerator(object):
    @cherrypy.expose
    def index(self):
        return '''
            <html>
                <head>
                    <title>Generator Link ke QR code</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f2f2f2;
                            color: #333;
                        }
                        h1 {
                            text-align: center;
                            margin-top: 50px;
                            margin-bottom: 20px;
                        }
                        form {
                            width: 400px;
                            margin: 0 auto;
                            background-color: #fff;
                            border-radius: 5px;
                            padding: 20px;
                            box-shadow: 0px 0px 10px #aaa;
                        }
                        input[type="text"] {
                            width: 100%;
                            padding: 10px;
                            font-size: 16px;
                            margin-bottom: 20px;
                            border-radius: 3px;
                            border: 1px solid #ccc;
                            box-sizing: border-box;
                        }
                        button[type="submit"] {
                            width: 100%;
                            background-color: #007bff;
                            color: #fff;
                            border: none;
                            border-radius: 3px;
                            padding: 10px;
                            font-size: 16px;
                            cursor: pointer;
                            transition: background-color 0.3s ease;
                        }
                        button[type="submit"]:hover {
                            background-color: #0069d9;
                        }
                        @media only screen and (max-width: 768px) {
                         /* aturan CSS untuk tampilan smartphone */
}

                    </style>
                </head>
                <body>
                    <h1>Generator link ke Qr Code</h1>
                    <form method="post" action="/generate_qr">
                        <label for="link">Link to encode:</label>
                        <br>
                        <input type="text" name="link" id="link" placeholder="Masukkan Link disini">
                        <br>
                        <button type="submit">Generate QR Code</button>
                    </form>
                </body>
            </html>
        '''

    @cherrypy.expose
    def generate_qr(self, link):
        img = qrcode.make(link)
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        cherrypy.response.headers['Content-Type'] = 'image/png'
        return img_io.getvalue()

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.quickstart(QRGenerator())
